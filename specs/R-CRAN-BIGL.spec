%global packname  BIGL
%global packver   1.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.1
Release:          1%{?dist}
Summary:          Biochemically Intuitive Generalized Loewe Model

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-MASS 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-minpack.lm 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-CRAN-scales 
Requires:         R-CRAN-ggplot2 
Requires:         R-MASS 
Requires:         R-methods 
Requires:         R-CRAN-minpack.lm 
Requires:         R-CRAN-numDeriv 
Requires:         R-parallel 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-robustbase 
Requires:         R-CRAN-scales 

%description
Response surface methods for drug synergy analysis. Available methods
include generalized and classical Loewe formulations as well as Highest
Single Agent methodology. Response surfaces can be plotted in an
interactive 3-D plot and formal statistical tests for presence of
synergistic effects are available. Implemented methods and tests are
described in the article "BIGL: Biochemically Intuitive Generalized Loewe
null model for prediction of the expected combined effect compatible with
partial agonism and antagonism" by Koen Van der Borght, Annelies Tourny,
Rytis Bagdziunas, Olivier Thas, Maxim Nazarov, Heather Turner, Bie Verbist
& Hugo Ceulemans (2017) <doi:10.1038/s41598-017-18068-5>.

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
