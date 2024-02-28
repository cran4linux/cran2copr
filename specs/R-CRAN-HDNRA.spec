%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  HDNRA
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          High-Dimensional Location Testing with Normal-Reference Approaches

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-expm 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-expm 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-readr 
Requires:         R-stats 

%description
We provide a collection of various classical tests and latest
normal-reference tests for comparing high-dimensional mean vectors
including two-sample and general linear hypothesis testing (GLHT) problem.
Some existing tests for two-sample problem [see Bai, Zhidong, and Hewa
Saranadasa.(1996) <https://www.jstor.org/stable/24306018>; Chen, Song Xi,
and Ying-Li Qin.(2010) <doi:10.1214/09-aos716>; Srivastava, Muni S., and
Meng Du.(2008) <doi:10.1016/j.jmva.2006.11.002>; Srivastava, Muni S.,
Shota Katayama, and Yutaka Kano.(2013)<doi:10.1016/j.jmva.2012.08.014>].
Normal-reference tests for two-sample problem [see Zhang, Jin-Ting, Jia
Guo, Bu Zhou, and Ming-Yen Cheng.(2020)
<doi:10.1080/01621459.2019.1604366>; Zhang, Jin-Ting, Bu Zhou, Jia Guo,
and Tianming Zhu.(2021) <doi:10.1016/j.jspi.2020.11.008>; Zhang, Liang,
Tianming Zhu, and Jin-Ting Zhang.(2020)
<doi:10.1016/j.ecosta.2019.12.002>; Zhang, Liang, Tianming Zhu, and
Jin-Ting Zhang.(2023) <doi:10.1080/02664763.2020.1834516>; Zhang,
Jin-Ting, and Tianming Zhu.(2022) <doi:10.1080/10485252.2021.2015768>;
Zhang, Jin-Ting, and Tianming Zhu.(2022) <doi:10.1007/s42519-021-00232-w>;
Zhu, Tianming, Pengfei Wang, and Jin-Ting Zhang.(2023)
<doi:10.1007/s00180-023-01433-6>]. Some existing tests for GLHT problem
[see Fujikoshi, Yasunori, Tetsuto Himeno, and Hirofumi Wakaki.(2004)
<doi:10.14490/jjss.34.19>; Srivastava, Muni S., and Yasunori
Fujikoshi.(2006) <doi:10.1016/j.jmva.2005.08.010>; Yamada, Takayuki, and
Muni S. Srivastava.(2012) <doi:10.1080/03610926.2011.581786>; Schott,
James R.(2007) <doi:10.1016/j.jmva.2006.11.007>; Zhou, Bu, Jia Guo, and
Jin-Ting Zhang.(2017) <doi:10.1016/j.jspi.2017.03.005>]. Normal-reference
tests for GLHT problem [see Zhang, Jin-Ting, Jia Guo, and Bu Zhou.(2017)
<doi:10.1016/j.jmva.2017.01.002>; Zhang, Jin-Ting, Bu Zhou, and Jia
Guo.(2022) <doi:10.1016/j.jmva.2021.104816>; Zhu, Tianming, Liang Zhang,
and Jin-Ting Zhang.(2022) <doi:10.5705/ss.202020.0362>; Zhu, Tianming, and
Jin-Ting Zhang.(2022) <doi:10.1007/s00180-021-01110-6>; Zhang, Jin-Ting,
and Tianming Zhu.(2022) <doi:10.1016/j.csda.2021.107385>].

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
