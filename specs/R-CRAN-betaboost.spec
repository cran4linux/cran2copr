%global __brp_check_rpaths %{nil}
%global packname  betaboost
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          3%{?dist}%{?buildtag}
Summary:          Boosting Beta Regression

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-mboost 
BuildRequires:    R-CRAN-gamboostLSS 
Requires:         R-CRAN-mboost 
Requires:         R-CRAN-gamboostLSS 

%description
Implements boosting beta regression for potentially high-dimensional data
(Mayr et al., 2018 <doi:10.1093/ije/dyy093>). The 'betaboost' package uses
the same parametrization as 'betareg' (Cribari-Neto and Zeileis, 2010
<doi:10.18637/jss.v034.i02>) to make results directly comparable. The
underlying algorithms are implemented via the R add-on packages 'mboost'
(Hofner et al., 2014 <doi:10.1007/s00180-012-0382-5>) and 'gamboostLSS'
(Mayr et al., 2012 <doi:10.1111/j.1467-9876.2011.01033.x>).

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX
