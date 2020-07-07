%global packname  future.BatchJobs
%global packver   0.16.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.16.2
Release:          3%{?dist}
Summary:          A Future API for Parallel and Distributed Processing usingBatchJobs

License:          LGPL (>= 2.1)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-BatchJobs >= 1.8
BuildRequires:    R-CRAN-future >= 1.14.0
BuildRequires:    R-CRAN-R.utils 
Requires:         R-CRAN-BatchJobs >= 1.8
Requires:         R-CRAN-future >= 1.14.0
Requires:         R-CRAN-R.utils 

%description
Implementation of the Future API on top of the 'BatchJobs' package. This
allows you to process futures, as defined by the 'future' package, in
parallel out of the box, not only on your local machine or ad-hoc cluster
of machines, but also via high-performance compute ('HPC') job schedulers
such as 'LSF', 'OpenLava', 'Slurm', 'SGE', and 'TORQUE' / 'PBS', e.g. 'y
<- future.apply::future_lapply(files, FUN = process)'. NOTE: The
'BatchJobs' package is deprecated in favor of the 'batchtools' package.
Because of this, it is recommended to use the 'future.batchtools' package
instead of this package.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/conf
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
