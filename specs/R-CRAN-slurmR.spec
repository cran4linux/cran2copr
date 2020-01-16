%global packname  slurmR
%global packver   0.3-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}
Summary:          A Lightweight Wrapper for 'Slurm'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-parallel 
BuildRequires:    R-utils 
Requires:         R-parallel 
Requires:         R-utils 

%description
'Slurm', Simple Linux Utility for Resource Management
<https://slurm.schedmd.com/>, is a popular 'Linux' based software used to
schedule jobs in 'HPC' (High Performance Computing) clusters. This R
package provides a specialized lightweight wrapper of 'Slurm' with a
syntax similar to that found in the 'parallel' R package. The package also
includes a method for creating socket cluster objects spanning multiple
nodes that can be used with the 'parallel' package.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/example.R
%doc %{rlibdir}/%{packname}/example.slurm
%doc %{rlibdir}/%{packname}/tinytest
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
