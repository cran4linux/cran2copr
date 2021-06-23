%global __brp_check_rpaths %{nil}
%global packname  AnthropMMD
%global packver   3.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          An R Package for Smith's Mean Measure of Divergence (MMD)

License:          CeCILL-2 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-scatterplot3d 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-smacof 
Requires:         R-CRAN-plotrix 
Requires:         R-CRAN-scatterplot3d 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-smacof 

%description
Offers a graphical user interface for the calculation of the mean measure
of divergence, with facilities for trait selection and graphical
representations <doi:10.1002/ajpa.23336>.

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
