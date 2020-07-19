%global packname  CsChange
%global packver   0.1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.6
Release:          1%{?dist}
Summary:          Testing for Change in C-Statistic

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rms 
BuildRequires:    R-survival 
BuildRequires:    R-boot 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Hmisc 
Requires:         R-CRAN-rms 
Requires:         R-survival 
Requires:         R-boot 
Requires:         R-stats 
Requires:         R-CRAN-Hmisc 

%description
Calculate the confidence interval and p value for change in C-statistic.
The adjusted C-statistic is calculated by using formula as "Somers' Dxy
rank correlation"/2+0.5. The confidence interval was calculated by using
the bootstrap method. The p value was calculated by using the Z testing
method. Please refer to the article of Peter Ganz et al. (2016)
<doi:10.1001/jama.2016.5951>.

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
