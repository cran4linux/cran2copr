%global packname  gpairs
%global packver   1.3.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.3
Release:          1%{?dist}
Summary:          The Generalized Pairs Plot

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-barcode 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-vcd 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-colorspace 
Requires:         R-grid 
Requires:         R-CRAN-barcode 
Requires:         R-lattice 
Requires:         R-CRAN-vcd 
Requires:         R-MASS 
Requires:         R-CRAN-colorspace 

%description
Offers a generalization of the scatterplot matrix based on the recognition
that most datasets include both categorical and quantitative information.
Traditional grids of scatterplots often obscure important features of the
data when one or more variables are categorical but coded as numerical.
The generalized pairs plot offers a range of displays of paired
combinations of categorical and quantitative variables. Emerson et al.
(2013) <DOI:10.1080/10618600.2012.694762>.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
