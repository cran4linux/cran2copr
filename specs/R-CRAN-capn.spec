%global packname  capn
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}
Summary:          Capital Asset Pricing for Nature

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.1
Requires:         R-core >= 3.0.1
BuildArch:        noarch

%description
Implements approximation methods for natural capital asset prices
suggested by Fenichel and Abbott (2014) <doi:10.1086/676034> in Journal of
the Associations of Environmental and Resource Economists (JAERE),
Fenichel et al. (2016) <doi:10.1073/pnas.1513779113> in Proceedings of the
National Academy of Sciences (PNAS), and Yun et al. (2017) in PNAS
(accepted), and their extensions: creating Chebyshev polynomial nodes and
grids, calculating basis of Chebyshev polynomials, approximation and their
simulations for: V-approximation (single and multiple stocks, PNAS),
P-approximation (single stock, PNAS), and Pdot-approximation (single
stock, JAERE). Development of this package was generously supported by the
Knobloch Family Foundation.

%prep
%setup -q -c -n %{packname}


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
%{rlibdir}/%{packname}/data
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
