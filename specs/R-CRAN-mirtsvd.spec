%global __brp_check_rpaths %{nil}
%global packname  mirtsvd
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          SVD-Based Estimation for Exploratory Item Factor Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildArch:        noarch
BuildRequires:    R-CRAN-GPArotation 
BuildRequires:    R-CRAN-mirtjml 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-CRAN-GPArotation 
Requires:         R-CRAN-mirtjml 
Requires:         R-graphics 
Requires:         R-stats 

%description
Provides singular value decomposition based estimation algorithms for
exploratory item factor analysis (IFA) based on multidimensional item
response theory models. For more information, please refer to: Zhang, H.,
Chen, Y., & Li, X. (2020). A note on exploratory item factor analysis by
singular value decomposition. Psychometrika, 1-15,
<DOI:10.1007/s11336-020-09704-7>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
