%global packname  BrasilMF
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Best Brazilian Financial Market Package

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-bizdays 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-rvest 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-xml2 
Requires:         R-CRAN-bizdays 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-rvest 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-xml2 

%description
Focuses on unifying the main data of the Brazilian financial market in one
package this will help the user to make the best investment decisions, for
more information <https://brasilmf.herokuapp.com>.

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
