%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rutledge
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Real-Time PCR Data Sets by Rutledge et al. (2004)

License:          CC BY 4.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-tibble 

%description
Real-time quantitative polymerase chain reaction (qPCR) data by Rutledge
et al. (2004) <doi:10.1093/nar/gnh177> in tidy format. The data comprises
a six-point, ten-fold dilution series, repeated in five independent runs,
for two different amplicons. In each run, each standard concentration is
replicated four times. Original raw data file:
<https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/nar/32/22/10.1093_nar_gnh177/1/gnh177_Supplementary_Data.zip?Expires=1680370010&Signature=xxk4VxX0C4yr3UWzxgh7ieCt7QQmpFMRauvsVEwtGXYGCcyQY7uhNCE-M8zx9kpyDPoS8NR7fjBuMx2Xz2ANFwF1VqnjQ4AfO37klnJ3CHRIJ7bj01n2mycHDnvJ3XawHdWT8TqJxTxVC9CpYEkH2xGeJBnnpcnXLbc94A8KB8FCtg2WR3O~ULkaOQQ8uJAiVdJhnBHH~XfBRkfoKHSuyJgX7n7M2~gwXnZH9n3vUyo~CHrpIax7Hi0xUSCBbQM571hxA7JIHkhZ0HBm2aXFuAru2yJ~o8jMEnnguOJg8T7mGqTDzUBtW0hJhmQDksdJoyeAFzU84QRUIZj9q3-tXg__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA>.

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
