%global packname  future.batchtools
%global packver   0.9.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.0
Release:          3%{?dist}
Summary:          A Future API for Parallel and Distributed Processing using'batchtools'

License:          LGPL (>= 2.1)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-future >= 1.14.0
BuildRequires:    R-CRAN-batchtools >= 0.9.11
BuildRequires:    R-utils 
Requires:         R-CRAN-future >= 1.14.0
Requires:         R-CRAN-batchtools >= 0.9.11
Requires:         R-utils 

%description
Implementation of the Future API on top of the 'batchtools' package. This
allows you to process futures, as defined by the 'future' package, in
parallel out of the box, not only on your local machine or ad-hoc cluster
of machines, but also via high-performance compute ('HPC') job schedulers
such as 'LSF', 'OpenLava', 'Slurm', 'SGE', and 'TORQUE' / 'PBS', e.g. 'y
<- future.apply::future_lapply(files, FUN = process)'.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/templates
%doc %{rlibdir}/%{packname}/templates-for-R_CMD_check
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
