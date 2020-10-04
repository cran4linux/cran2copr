%global packname  inferference
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}%{?buildtag}
Summary:          Methods for Causal Inference with Interference

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildArch:        noarch
BuildRequires:    R-CRAN-numDeriv >= 2012.9.1
BuildRequires:    R-CRAN-lme4 >= 1.1.6
BuildRequires:    R-CRAN-Formula >= 1.1.2
BuildRequires:    R-methods 
Requires:         R-CRAN-numDeriv >= 2012.9.1
Requires:         R-CRAN-lme4 >= 1.1.6
Requires:         R-CRAN-Formula >= 1.1.2
Requires:         R-methods 

%description
Provides methods for estimating causal effects in the presence of
interference described in B. Saul and M. Hugdens (2017)
<doi:10.18637/jss.v082.i02>. Currently it implements the
inverse-probability weighted (IPW) estimators proposed by E.J. Tchetgen
Tchetgen and T.J. Vanderweele (2012) <doi:10.1177/0962280210386779>.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
