%global __brp_check_rpaths %{nil}
%global packname  WLinfer
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Inference in Weighted Lindley Distribution

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-LindleyR 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-boot 
BuildRequires:    R-CRAN-nleqslv 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-goftest 
BuildRequires:    R-CRAN-cubature 
BuildRequires:    R-CRAN-bbmle 
Requires:         R-CRAN-LindleyR 
Requires:         R-CRAN-pracma 
Requires:         R-boot 
Requires:         R-CRAN-nleqslv 
Requires:         R-stats 
Requires:         R-CRAN-goftest 
Requires:         R-CRAN-cubature 
Requires:         R-CRAN-bbmle 

%description
Estimate the parameters of weighted Lindley distribution, and provide some
useful results like goodness of fit or confidence interval etc. Ghitany,
M., Alqallaf, F., Al-Mutairi, D., Husain, H. (2011)
<doi:10.1016/j.matcom.2010.11.005>. Hyoung-Moon Kim. and Yu-Hyeong Jang.
(2020) submitted. Wang, M., Wang, W. (2017)
<doi:10.1080/03610918.2014.970696>.

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
