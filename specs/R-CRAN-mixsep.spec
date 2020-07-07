%global packname  mixsep
%global packver   0.2.1-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1.2
Release:          2%{?dist}
Summary:          Forensic Genetics DNA Mixture Separation

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.0.0
Requires:         R-core >= 2.0.0
BuildArch:        noarch
BuildRequires:    R-tcltk 
BuildRequires:    R-CRAN-tcltk2 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-RODBC 
Requires:         R-tcltk 
Requires:         R-CRAN-tcltk2 
Requires:         R-MASS 
Requires:         R-CRAN-RODBC 

%description
Separates DNA mixtures using a statistical model within a greedy algorithm
with a useful tcl/tk GUI.

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

%files
%{rlibdir}/%{packname}
