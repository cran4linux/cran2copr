%global packname  ActCR
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          2%{?dist}%{?buildtag}
Summary:          Extract Circadian Rhythms Metrics from Actigraphy Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-cosinor 
BuildRequires:    R-CRAN-cosinor2 
BuildRequires:    R-CRAN-dplyr 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-cosinor 
Requires:         R-CRAN-cosinor2 
Requires:         R-CRAN-dplyr 

%description
Circadian rhythms are rhythms that oscillate about every 24 h, which has
been observed in multiple physiological processes including core body
temperature, hormone secretion, heart rate, blood pressure, and many
others. Measuring circadian rhythm with wearables is based on a principle
that there is increased movement during wake periods and reduced movement
during sleep periods, and has been shown to be reliable and valid. This
package can be used to extract nonparametric circadian metrics like
intradaily variability (IV), interdaily stability (IS), and relative
amplitude (RA); and parametric cosinor model coefficient. Details can be
found in Junrui Di et al (2019) <doi:10.1007/s12561-019-09236-4>.

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
