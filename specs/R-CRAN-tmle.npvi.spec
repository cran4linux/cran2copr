%global __brp_check_rpaths %{nil}
%global packname  tmle.npvi
%global packver   0.10.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.10.0
Release:          3%{?dist}%{?buildtag}
Summary:          Targeted Learning of a NP Importance of a Continuous Exposure

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-R.utils >= 1.4.1
BuildRequires:    R-CRAN-R.methodsS3 
BuildRequires:    R-CRAN-R.oo 
BuildRequires:    R-MASS 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-geometry 
Requires:         R-CRAN-R.utils >= 1.4.1
Requires:         R-CRAN-R.methodsS3 
Requires:         R-CRAN-R.oo 
Requires:         R-MASS 
Requires:         R-Matrix 
Requires:         R-CRAN-geometry 

%description
Targeted minimum loss estimation (TMLE) of a non-parametric variable
importance measure of a continuous exposure 'X' on an outcome 'Y', taking
baseline covariates 'W' into account.

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
%doc %{rlibdir}/%{packname}/NEWS
%doc %{rlibdir}/%{packname}/system
%doc %{rlibdir}/%{packname}/testScripts
%{rlibdir}/%{packname}/INDEX
