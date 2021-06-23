%global __brp_check_rpaths %{nil}
%global packname  fcr
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Functional Concurrent Regression for Sparse Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.4
Requires:         R-core >= 3.2.4
BuildArch:        noarch
BuildRequires:    R-CRAN-fields >= 9.0
BuildRequires:    R-mgcv >= 1.7
BuildRequires:    R-CRAN-face >= 0.1
Requires:         R-CRAN-fields >= 9.0
Requires:         R-mgcv >= 1.7
Requires:         R-CRAN-face >= 0.1

%description
Dynamic prediction in functional concurrent regression with an application
to child growth. Extends the pffr() function from the 'refund' package to
handle the scenario where the functional response and concurrently
measured functional predictor are irregularly measured.  Leroux et al.
(2017), Statistics in Medicine, <doi:10.1002/sim.7582>.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
