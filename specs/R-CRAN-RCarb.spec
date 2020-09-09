%global packname  RCarb
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Dose Rate Modelling of Carbonate-Rich Samples

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-interp >= 1.0
BuildRequires:    R-CRAN-matrixStats >= 0.54.0
BuildRequires:    R-utils 
Requires:         R-CRAN-interp >= 1.0
Requires:         R-CRAN-matrixStats >= 0.54.0
Requires:         R-utils 

%description
Translation of the 'MATLAB' program 'Carb' (Nathan and Mauz 2008
<DOI:10.1016/j.radmeas.2007.12.012>; Mauz and Hoffmann 2014) for dose rate
modelling for carbonate-rich samples in the context of trapped charged
dating (e.g., luminescence dating) applications.

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
