%global __brp_check_rpaths %{nil}
%global packname  moc
%global packver   2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0
Release:          3%{?dist}%{?buildtag}
Summary:          General Nonlinear Multivariate Finite Mixtures

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0

%description
Fits and vizualize user defined finite mixture models for multivariate
observations using maximum likelihood. (McLachlan, G., Peel, D. (2000)
Finite Mixture Models. Wiley-Interscience.)

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
%doc %{rlibdir}/%{packname}/Changes
%doc %{rlibdir}/%{packname}/Examples
%doc %{rlibdir}/%{packname}/GPL
%doc %{rlibdir}/%{packname}/GUI
%doc %{rlibdir}/%{packname}/Sweave
%doc %{rlibdir}/%{packname}/Utils
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
