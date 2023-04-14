%global __brp_check_rpaths %{nil}
%global packname  corkscrew
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Preprocessor for Data Modeling

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.1
Requires:         R-core >= 3.0.1
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gplots 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gplots 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-igraph 
Requires:         R-stats 
Requires:         R-grDevices 

%description
Includes binning categorical variables into lesser number of categories
based on t-test, converting categorical variables into continuous features
using the mean of the response variable for the respective categories,
understanding the relationship between the response variable and predictor
variables using data transformations.

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
