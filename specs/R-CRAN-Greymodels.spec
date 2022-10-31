%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Greymodels
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Shiny App for Grey Forecasting Model

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-Metrics 
BuildRequires:    R-CRAN-cmna 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-CRAN-shinyWidgets 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-particle.swarm.optimisation 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-expm 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-Metrics 
Requires:         R-CRAN-cmna 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinydashboard 
Requires:         R-CRAN-shinyWidgets 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-particle.swarm.optimisation 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-expm 

%description
The 'Greymodels' Shiny app is an interactive interface for statistical
modelling and forecasting using grey-based models. It covers several
state-of-the-art univariate and multivariate grey models. A user friendly
interface allows users to easily compare the performance of different
models for prediction and among others, visualize graphical plots of
predicted values within user chosen confidence intervals. Chang, C. (2019)
<doi:10.24818/18423264/53.1.19.11>, Li, K., Zhang, T. (2019)
<doi:10.1007/s12667-019-00344-0>, Ou, S. (2012)
<doi:10.1016/j.compag.2012.03.007>, Li, S., Zhou, M., Meng, W., Zhou, W.
(2019) <doi:10.1080/23307706.2019.1666310>, Xie, N., Liu, S. (2009)
<doi:10.1016/j.apm.2008.01.011>, Shao, Y., Su, H. (2012)
<doi:10.1016/j.aasri.2012.06.003>, Xie, N., Liu, S., Yang, Y., Yuan, C.
(2013) <doi:10.1016/j.apm.2012.10.037>, Li, S., Miao, Y., Li, G., Ikram,
M. (2020) <doi:10.1016/j.matcom.2019.12.020>, Che, X., Luo, Y., He, Z.
(2013) <doi:10.4028/www.scientific.net/AMM.364.207>, Zhu, J., Xu, Y.,
Leng, H., Tang, H., Gong, H., Zhang, Z. (2016)
<doi:10.1109/appeec.2016.7779929>, Luo, Y., Liao, D. (2012)
<doi:10.4028/www.scientific.net/AMR.507.265>, Bilgil, H. (2020)
<doi:10.3934/math.2021091>, Li, D., Chang, C., Chen, W., Chen, C. (2011)
<doi:10.1016/j.apm.2011.04.006>, Chen, C. (2008)
<doi:10.1016/j.chaos.2006.08.024>, Zhou, W., Pei, L. (2020)
<doi:10.1007/s00500-019-04248-0>, Xiao, X., Duan, H. (2020)
<doi:10.1016/j.engappai.2019.103350>, Xu, N., Dang, Y. (2015)
<doi:10.1155/2015/606707>, Chen, P., Yu, H.(2014)
<doi:10.1155/2014/242809>, Zeng, B., Li, S., Meng, W., Zhang, D. (2019)
<doi:10.1371/journal.pone.0221333>, Liu, L., Wu, L. (2021)
<doi:10.1016/j.apm.2020.08.080>, Hu, Y. (2020)
<doi:10.1007/s00500-020-04765-3>, Zhou, P., Ang, B., Poh, K. (2006)
<doi:10.1016/j.energy.2005.12.002>, Cheng, M., Li, J., Liu, Y., Liu, B.
(2020) <doi:10.3390/su12020698>, Wang, H., Wang, P., Senel, M., Li, T.
(2019) <doi:10.1155/2019/9049815>, Ding, S., Li, R. (2020)
<doi:10.1155/2020/4564653>, Zeng, B., Li, C. (2018)
<doi:10.1016/j.cie.2018.02.042>, Xie, N., Liu, S. (2015)
<doi:10.1109/JSEE.2015.00013>, Zeng, X., Yan, S., He, F., Shi, Y. (2019)
<doi:10.1016/j.apm.2019.11.032>.

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
