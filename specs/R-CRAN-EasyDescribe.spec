%global __brp_check_rpaths %{nil}
%global packname  EasyDescribe
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          A Convenient Way of Descriptive Statistics

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-multiCA 
BuildRequires:    R-CRAN-CATT 
BuildRequires:    R-CRAN-gmodels 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-rcompanion 
BuildRequires:    R-CRAN-FSA 
BuildRequires:    R-CRAN-fitdistrplus 
BuildRequires:    R-CRAN-nortest 
Requires:         R-CRAN-multiCA 
Requires:         R-CRAN-CATT 
Requires:         R-CRAN-gmodels 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-rcompanion 
Requires:         R-CRAN-FSA 
Requires:         R-CRAN-fitdistrplus 
Requires:         R-CRAN-nortest 

%description
Descriptive Statistics is essential for publishing articles. This package
can perform descriptive statistics according to different data types. If
the data is a continuous variable, the mean and standard deviation or
median and quartiles are automatically output; if the data is a
categorical variable, the number and percentage are automatically output.
In addition, if you enter two variables, the first variable will be
described hierarchically based on the second variable and the statistical
differences between different groups will be compared using appropriate
statistical methods. And for groups more than two, the post hoc test will
be applied. For more information on the methods we used, please see the
following references: Libiseller, C. and Grimvall, A. (2002)
<doi:10.1002/env.507>, Patefield, W. M. (1981) <doi:10.2307/2346669>,
Hope, A. C. A. (1968) <doi:10.1111/J.2517-6161.1968.TB00759.X>, Mehta, C.
R. and Patel, N. R. (1983) <doi:10.1080/01621459.1983.10477989>, Mehta, C.
R. and Patel, N. R. (1986) <doi:10.1145/6497.214326>, Clarkson, D. B.,
Fan, Y. and Joe, H. (1993) <doi:10.1145/168173.168412>, Cochran, W. G.
(1954) <doi:10.2307/3001616>, Armitage, P. (1955) <doi:10.2307/3001775>,
Szabo, A. (2016) <doi:10.1080/00031305.2017.1407823>, David, F. B. (1972)
<doi:10.1080/01621459.1972.10481279>, Joanes, D. N. and Gill, C. A. (1998)
<doi:10.1111/1467-9884.00122>, Dunn, O. J. (1964)
<doi:10.1080/00401706.1964.10490181>, Copenhaver, M. D. and Holland, B. S.
(1988) <doi:10.1080/00949658808811082>, Chambers, J. M., Freeny, A. and
Heiberger, R. M. (1992) <doi:10.1201/9780203738535-5>, Shaffer, J. P.
(1995) <doi:10.1146/annurev.ps.46.020195.003021>, Myles, H. and Douglas,
A. W. (1973) <doi:10.2307/2063815>, Rahman, M. and Tiwari, R. (2012)
<doi:10.4236/health.2012.410139>. Thode, H. J. (2002)
<doi:10.1201/9780203910894>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
