%global __brp_check_rpaths %{nil}
%global packname  modifiedmk
%global packver   1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6
Release:          1%{?dist}%{?buildtag}
Summary:          Modified Versions of Mann Kendall and Spearman's Rho Trend Tests

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-boot 
Requires:         R-CRAN-boot 

%description
Power of non-parametric Mann-Kendall test and Spearman’s Rho test is
highly influenced by serially correlated data. To address this issue,
trend tests may be applied on the modified versions of the time series
data by Block Bootstrapping (BBS), Prewhitening (PW) , Trend Free
Prewhitening (TFPW), Bias Corrected Prewhitening and Variance Correction
Approach by calculating effective sample size. Mann, H. B.
(1945).<doi:10.1017/CBO9781107415324.004>. Kendall, M. (1975).
Multivariate analysis. Charles Griffin&Company Ltd,. sen, P. K.
(1968).<doi:10.2307/2285891>. Önöz, B., & Bayazit, M. (2012)
<doi:10.1002/hyp.8438>. Hamed, K. H.
(2009).<doi:10.1016/j.jhydrol.2009.01.040>. Yue, S., & Wang, C. Y. (2002)
<doi:10.1029/2001WR000861>. Yue, S., Pilon, P., Phinney, B., & Cavadias,
G. (2002) <doi:10.1002/hyp.1095>. Hamed, K. H., & Ramachandra Rao, A.
(1998) <doi:10.1016/S0022-1694(97)00125-X>. Yue, S., & Wang, C. Y. (2004)
<doi:10.1023/B:WARM.0000043140.61082.60>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
