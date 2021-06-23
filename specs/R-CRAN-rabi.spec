%global __brp_check_rpaths %{nil}
%global packname  rabi
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Generate Codes to Uniquely and Robustly Identify Individuals for Animal Behavior Studies

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.5
Requires:         R-core >= 3.2.5
BuildArch:        noarch
BuildRequires:    R-CRAN-numbers 
BuildRequires:    R-CRAN-polynom 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-stringdist 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
Requires:         R-CRAN-numbers 
Requires:         R-CRAN-polynom 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-stringdist 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-methods 

%description
Facilitates the design and generation of optimal color (or symbol) codes
that can be used to mark and identify individual animals. These codes are
made such that the IDs are robust to partial erasure: even if sections of
the code are lost, the entire identity of the animal can be reconstructed.
Thus, animal subjects are not confused and no ambiguity is introduced.

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
