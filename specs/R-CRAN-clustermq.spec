%global packname  clustermq
%global packver   0.8.8.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.8.1
Release:          1%{?dist}
Summary:          Evaluate Function Calls on HPC Schedulers (LSF, SGE, SLURM,PBS/Torque)

License:          Apache License (== 2.0) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-CRAN-rzmq >= 0.9.4
BuildRequires:    R-CRAN-narray 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-utils 
Requires:         R-CRAN-rzmq >= 0.9.4
Requires:         R-CRAN-narray 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-R6 
Requires:         R-utils 

%description
Evaluate arbitrary function calls using workers on HPC schedulers in
single line of code. All processing is done on the network without
accessing the file system. Remote schedulers are supported via SSH.

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/LSF.tmpl
%doc %{rlibdir}/%{packname}/PBS.tmpl
%doc %{rlibdir}/%{packname}/SGE.tmpl
%doc %{rlibdir}/%{packname}/SLURM.tmpl
%doc %{rlibdir}/%{packname}/SSH.tmpl
%doc %{rlibdir}/%{packname}/TORQUE.tmpl
%{rlibdir}/%{packname}/INDEX
