%global packname  MALDIrppa
%global packver   1.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.5
Release:          1%{?dist}%{?buildtag}
Summary:          MALDI Mass Spectrometry Data Robust Pre-Processing and Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.5
Requires:         R-core >= 3.2.5
BuildRequires:    R-CRAN-MALDIquant 
BuildRequires:    R-CRAN-signal 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-lattice 
Requires:         R-CRAN-MALDIquant 
Requires:         R-CRAN-signal 
Requires:         R-CRAN-robustbase 
Requires:         R-lattice 

%description
Provides methods for quality control and robust pre-processing and
analysis of MALDI mass spectrometry data (Palarea-Albaladejo et al. (2018)
<doi:10.1093/bioinformatics/btx628>).

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
