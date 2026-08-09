%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cpge
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Career Possibilities after French Selective Engineering Schools in France

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-quarto 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-visNetwork 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-quarto 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-visNetwork 

%description
To help French students from Classes Preparatoires aux Grandes Ecoles
(CPGE) in their choice of field of study and career options, this package
provides an interactive tool and data visualization of a graph clustered
by different competitive exams and sectors of activity for French
selective engineering schools and selective higher education institutions
like Ecoles Normales Superieures (ENS) or specialized university programs.
Besides, there are two drop-down menus to select on the graph many fields
or more than 200 engineering schools or ENS. It gives the opportunity to
expand, collapse clusters of selective exams interactively too. For more
information, see the demonstration video:
<https://valerierobert-maths.re/index.php/maths-en-cpge/>. The data was
collected via the official French website:
<https://www.scei-concours.fr/statistiques.html>.

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
