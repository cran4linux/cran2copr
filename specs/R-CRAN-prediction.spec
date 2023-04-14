%global __brp_check_rpaths %{nil}
%global packname  prediction
%global packver   0.3.14
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.14
Release:          3%{?dist}%{?buildtag}
Summary:          Tidy, Type-Safe 'prediction()' Methods

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-data.table 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-data.table 

%description
A one-function package containing 'prediction()', a type-safe alternative
to 'predict()' that always returns a data frame. The 'summary()' method
provides a data frame with average predictions, possibly over
counterfactual versions of the data (a la the 'margins' command in
'Stata'). Marginal effect estimation is provided by the related package,
'margins' <https://cran.r-project.org/package=margins>. The package
currently supports common model types (e.g., "lm", "glm") from the 'stats'
package, as well as numerous other model classes from other add-on
packages. See the README or main package documentation page for a complete
listing.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
