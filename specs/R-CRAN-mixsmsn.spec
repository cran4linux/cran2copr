%global packname  mixsmsn
%global packver   1.1-6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.6
Release:          1%{?dist}
Summary:          Fitting Finite Mixture of Scale Mixture of Skew-NormalDistributions

License:          GPL (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 1.9.0
Requires:         R-core >= 1.9.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mvtnorm >= 0.9.9
Requires:         R-CRAN-mvtnorm >= 0.9.9

%description
Functions to fit finite mixture of scale mixture of skew-normal (FM-SMSN)
distributions, details in Prates, Lachos and Cabral (2013) <doi:
10.18637/jss.v054.i12>, Cabral, Lachos and Prates (2012)
<doi:10.1016/j.csda.2011.06.026> and Basso, Lachos, Cabral and Ghosh
(2010) <doi:10.1016/j.csda.2009.09.031>.

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
%{rlibdir}/%{packname}/INDEX
