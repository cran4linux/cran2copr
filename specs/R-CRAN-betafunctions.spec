%global packname  betafunctions
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          3%{?dist}
Summary:          Functions for Working with Two- And Four-Parameter BetaProbability Distributions

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Package providing a number of functions for working with the Two- and
Four- parameter Beta distributions, including alternative
parameterizations and calculation of moments. Includes functions for
estimating classification accuracy, diagnostic performance and
consistency, using what's known as the Livingston and Lewis approach in
the educational-measurement literature as the base method. Livingston and
Lewis (1995) <doi:10.1111/j.1745-3984.1995.tb00462.x>. Hanson (1991)
<https://files.eric.ed.gov/fulltext/ED344945.pdf>. Glas, Lijmer, Prins,
Bonsel and Bossuyt (2003) <doi:10.1016/S0895-4356(03)00177-X>.

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
%{rlibdir}/%{packname}/INDEX
