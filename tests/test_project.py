import importlib.util,json,math,tempfile,shutil,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
lab=module('lab',ROOT/'code/resource_lab.py');checker=module('checker',ROOT/'scripts/check_coverage.py')
class ResourceTests(unittest.TestCase):
    def test_reference_storage(self):
        self.assertEqual(lab.tensor_bytes((1024,4096),16),8388608)
        self.assertEqual(lab.tensor_bytes((3,),4),2)
        self.assertEqual(lab.kv_bytes(1,2048,12,4,64),25165824)
    def test_shift_invariance(self):
        a=lab.softmax([2,1,0,-1]);b=lab.softmax([10002,10001,10000,9999])
        self.assertAlmostEqual(sum(a),1)
        for x,y in zip(a,b):self.assertAlmostEqual(x,y)
        self.assertAlmostEqual(-math.log(a[0]),0.44018969856)
    def test_sampler(self):
        self.assertEqual(lab.sample([0,1,0]),1)
        with self.assertRaises(ValueError):lab.sample([0.2,0.2])
class MicrogradTests(unittest.TestCase):
    def test_chain_rule_and_shared_paths(self):
        m=module('micrograd_test',ROOT/'code/micrograd.py')
        a,b,c=m.Value(2),m.Value(-3),m.Value(10);loss=m.expression(a,b,c);loss.backward()
        self.assertEqual(loss.data,16);self.assertEqual([a.grad,b.grad,c.grad],[-24,16,8])
        x,y=m.Value(3),m.Value(4);z=x*x+x*y;z.backward();self.assertEqual(x.grad,10);self.assertEqual(y.grad,3)
class EnvironmentTests(unittest.TestCase):
    def test_environment_record_is_json_and_excludes_environment(self):
        import subprocess
        out=subprocess.run([__import__('sys').executable,str(ROOT/'code/environment_record.py')],capture_output=True,text=True,check=True).stdout
        data=json.loads(out)
        self.assertIn('python',data);self.assertIn('packages',data)
        self.assertNotIn('environment',data)
class CoverageTests(unittest.TestCase):
    def test_project_and_release_gate(self):
        self.assertEqual(checker.validate()[0],[])
        self.assertTrue(checker.validate(release=True)[0])
    def test_missing_mapping_is_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            r=Path(d)/'project';shutil.copytree(ROOT,r,ignore=shutil.ignore_patterns('build','__pycache__'))
            p=r/'curriculum/source_inventory.json';data=json.loads(p.read_text());data[0]['chapter']='CH-999';p.write_text(json.dumps(data))
            self.assertTrue(any('Unmapped source' in e for e in checker.validate(r)[0]))
    def test_missing_anchor_is_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            r=Path(d)/'project';shutil.copytree(ROOT,r,ignore=shutil.ignore_patterns('build','__pycache__'))
            c=json.loads((r/'curriculum/chapters.json').read_text())[0];p=r/c['path'];p.write_text(p.read_text().replace('id="t-01-01"','id="gone"'))
            self.assertTrue(any('Missing section anchor' in e for e in checker.validate(r)[0]))
if __name__=='__main__':unittest.main()
