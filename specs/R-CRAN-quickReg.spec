%global packname  quickReg
%global packver   1.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.0
Release:          2%{?dist}
Summary:          Build Regression Models Quickly and Display the Results Using'ggplot2'

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 2.0.0
BuildRequires:    R-CRAN-rlang >= 0.1.2
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-nortest 
BuildRequires:    R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 >= 2.0.0
Requires:         R-CRAN-rlang >= 0.1.2
Requires:         R-survival 
Requires:         R-CRAN-psych 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-nortest 
Requires:         R-CRAN-dplyr 

%description
A set of functions to extract results from regression models and plot the
effect size using 'ggplot2' seamlessly. While 'broom' is useful to convert
statistical analysis objects into tidy data frames, 'coefplot' is adept at
showing multivariate regression results. With specific outcome, this
package could build regression models automatically, extract results into
a data frame and provide a quicker way to summarize models' statistical
findings using 'ggplot2'.

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

%files
%{rlibdir}/%{packname}
