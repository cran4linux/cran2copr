%global packname  reproj
%global packver   0.4.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.2
Release:          3%{?dist}
Summary:          Coordinate System Transformations for Generic Map Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.5
Requires:         R-core >= 3.2.5
BuildArch:        noarch
BuildRequires:    R-CRAN-crsmeta >= 0.3.0
BuildRequires:    R-CRAN-PROJ >= 0.1.6
BuildRequires:    R-CRAN-proj4 
Requires:         R-CRAN-crsmeta >= 0.3.0
Requires:         R-CRAN-PROJ >= 0.1.6
Requires:         R-CRAN-proj4 

%description
Transform coordinates from a specified source to a specified target map
projection. This uses the 'PROJ' library directly, by wrapping the 'PROJ'
package (if functional), otherwise the 'proj4' package. The 'reproj()'
function is generic, methods may be added to remove the need for an
explicit source definition. If 'proj4' is in use 'reproj()' handles the
requirement for conversion of angular units where necessary. This is for
use primarily to transform generic data formats and direct leverage of the
underlying 'PROJ' library. (There are transformations that aren't possible
with 'PROJ' and that are provided by the 'GDAL' library, a limitation
which users of this package should be aware of.) The 'PROJ' library is
available at <https://proj.org/>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/rationale
%{rlibdir}/%{packname}/INDEX
