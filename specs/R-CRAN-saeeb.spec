%global packname  saeeb
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Small Area Estimation for Count Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-COUNT >= 1.3.4
BuildRequires:    R-MASS 
BuildRequires:    R-stats 
Requires:         R-CRAN-COUNT >= 1.3.4
Requires:         R-MASS 
Requires:         R-stats 

%description
Provides small area estimation for count data type and gives option
whether to use covariates in the estimation or not. By implementing
Empirical Bayes (EB) Poisson-Gamma model, each function returns EB
estimators and mean squared error (MSE) estimators for each area. The EB
estimators without covariates are obtained using the model proposed by
Clayton & Kaldor (1987) <doi:10.2307/2532003>, the EB estimators with
covariates are obtained using the model proposed by Wakefield (2006)
<doi:10.1093/biostatistics/kxl008> and the MSE estimators are obtained
using Jackknife method by Jiang et. al. (2002)
<doi:10.1214/aos/1043351257>.

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
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
