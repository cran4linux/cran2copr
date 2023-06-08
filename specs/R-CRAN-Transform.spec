%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Transform
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Transformations

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch

%description
Performs various statistical transformations; Box-Cox and Log (Box and
Cox, 1964) <doi:10.1111/j.2517-6161.1964.tb00553.x>, Glog (Durbin et al.,
2002) <doi:10.1093/bioinformatics/18.suppl_1.S105>, Neglog (Whittaker et
al., 2005) <doi:10.1111/j.1467-9876.2005.00520.x>, Reciprocal (Tukey,
1957), Log Shift (Feng et al., 2016) <doi:10.1002/sta4.104>,
Bickel-Docksum (Bickel and Doksum, 1981)
<doi:10.1080/01621459.1981.10477649>, Yeo-Johnson (Yeo and Johnson, 2000)
<doi:10.1093/biomet/87.4.954>, Square Root (Medina et al., 2019), Manly
(Manly, 1976) <doi:10.2307/2988129>, Modulus (John and Draper, 1980)
<doi:10.2307/2986305>, Dual (Yang, 2006)
<doi:10.1016/j.econlet.2006.01.011>, Gpower (Kelmansky et al., 2013)
<doi:10.1515/sagmb-2012-0030>. It also performs graphical approaches,
assesses the success of the transformation via tests and plots.

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
