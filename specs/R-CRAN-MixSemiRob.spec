%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MixSemiRob
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Mixture Models: Parametric, Semiparametric, and Robust

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-GoFKernel 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-mixtools 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-Rlab 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-CRAN-ucminf 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-quadprog 
Requires:         R-CRAN-GoFKernel 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-mixtools 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-Rlab 
Requires:         R-CRAN-robustbase 
Requires:         R-CRAN-ucminf 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-quadprog 

%description
Various functions to estimate parametric (Gaussian, T - distribution,
Laplace, Pareto, log-concave distribution and etc.), non-parametric
mixture models; Perform hypothesis testing, root selection and provide
treatment for label switching for mixture models; Estimate parameters for
mixture of regressions, proportion varying mixture of regressions and
robust mixture of regressions. The functions and their corresponding
reference paper are as follows: KDEEM: Ma, Y., Wang, S., Xu, L. et
al.(2021)<doi:10.1007/s11749-020-00725-z>; KDEEM.H/KDEEM.LSE: David R.
Hunter & Derek S. Young (2012)<doi:10.1080/10485252.2011.608430>;
RM2_mixreg: Yu C, Yao W, Chen K.(2017)<doi:10.1002/cjs.11310>;
mixlinrb_bi: Xiuqin Bai, Weixin Yao, John E.
Boyer(2012)<doi:10.1016/j.csda.2012.01.016>; trimmix: N. Neykov, P.
Filzmoser, R. Dimova, P. Neytchev,(2007)<doi:10.1016/j.csda.2006.12.024>;
mixlint: Weixin Yao, Yan Wei, Chun
Yu(2014)<doi:10.1016/j.csda.2013.07.019>; mixreg_Lap: Weixing Song, Weixin
Yao, Yanru Xing(2014)<doi:10.1016/j.csda.2013.06.022>; mixreg_CWRM:
Garcia-Escudero, L.A., Gordaliza, A., Greselin, F. et al.(2017)
<doi:10.1007/s11222-021-10061-3>; mphd:Jingjing Wu, Weixin Yao, Sijia
Xiang (2017)<doi:10.1080/00949655.2017.1318136>; EMlogconc/EMlogconcHD:
George T. Chang, Guenther
Walther(2007)<doi:10.1016/j.csda.2007.01.008>;Hypothesis_test: Supawadee
Wichitchan, Weixin Yao, Guangren
Yang(2019)<doi:10.1016/j.csda.2018.05.005>; mixscale: Sijia Xiang, Weixin
Yao, Byungtae Seo(2016)<doi:10.1016/j.csda.2016.06.001>;
sim/simonestep:Xiang, S., Yao, W.(2020)<doi:10.1007/s11634-020-00392-w>;
paretomix1: Huang, M., Yao, W., Wang, S., and Chen, Y.
(2018)<doi:10.1111/sjos.12316>;complhfrequency/distlatfrequency: Weixin
Yao (2015)<doi:10.1080/00949655.2013.859259>; MixReg_Pvary: Mian Huang and
Weixin Yao (2012)<doi:10.1080/01621459.2012.682541>; pfmix: Weixin
Yao(2010)<doi:10.1016/j.jspi.2010.02.004>; backfitlocal/backfitglobal:
Xiang, S., Yao, W.(2018)<doi:10.1007/s10463-016-0584-7>;mixbspline: Dziak,
J. J., Li, R., Tan, X., Shiffman, S., & Shiyko, M. P.
(2015)<doi:10.1037/met0000048>; root_selection: Supawadee Wichitchan,
Weixin Yao & Guangren Yang (2019)<doi:10.1080/03610926.2018.1481972>;
mixbino/mixbinosemi/mixbinosemionestep/mixbinosemifull:J. Cao and W.
Yao(2012)<https://www3.stat.sinica.edu.tw/sstest/oldpdf/A22n12.pdf>.

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
