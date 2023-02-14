%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  homnormal
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Tests of Homogeneity of Variances

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-huxtable >= 5.4.0
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-CRAN-huxtable >= 5.4.0
Requires:         R-stats 
Requires:         R-graphics 

%description
Most common exact, asymptotic and resample based tests are provided for
testing the homogeneity of variances of k normal distributions under
normality. These tests are Barlett, Bhandary & Dai, Brown & Forsythe,
Chang et al., Gokpinar & Gokpinar, Levene, Liu and Xu, Gokpinar. Also, a
data generation function from multiple normal distribution is provided
using any multiple normal parameters. Bartlett, M. S. (1937)
<doi:10.1098/rspa.1937.0109> Bhandary, M., & Dai, H. (2008)
<doi:10.1080/03610910802431011> Brown, M. B., & Forsythe, A. B.
(1974).<doi:10.1080/01621459.1974.10482955> Chang, C. H., Pal, N., & Lin,
J. J. (2017) <doi:10.1080/03610918.2016.1202277> Gokpinar E. & Gokpinar F.
(2017) <doi:10.1080/03610918.2014.955110> Liu, X., & Xu, X. (2010)
<doi:10.1016/j.spl.2010.05.017> Levene, H. (1960)
<https://cir.nii.ac.jp/crid/1573950400526848896> Gökpınar, E. (2020)
<doi:10.1080/03610918.2020.1800037>.

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
