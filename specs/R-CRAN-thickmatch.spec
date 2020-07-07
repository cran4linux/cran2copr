%global packname  thickmatch
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          3%{?dist}
Summary:          Threshold Matching for Thick Description for Optimal Matching inObservational Studies

License:          MIT+file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rcbalance 
BuildRequires:    R-stats 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-DiPs 
Requires:         R-CRAN-rcbalance 
Requires:         R-stats 
Requires:         R-MASS 
Requires:         R-CRAN-plyr 
Requires:         R-methods 
Requires:         R-CRAN-DiPs 

%description
Conducts several closest matched pairs to strengthen a matched
quantitative comparison of many pairs by thick description in
observational studies. Rosenbaum, P. R. (2017).
<doi:10.1080/10618600.2016.1152971>.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
