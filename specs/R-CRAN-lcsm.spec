%global packname  lcsm
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}
Summary:          Univariate and Bivariate Latent Change Score Modeling

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats >= 3.5.2
BuildRequires:    R-CRAN-ggplot2 >= 2.2.1
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-tibble >= 1.4.2
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-semPlot >= 1.1
BuildRequires:    R-CRAN-tidyr >= 0.8.0
BuildRequires:    R-CRAN-dplyr >= 0.7.4
BuildRequires:    R-CRAN-lavaan >= 0.6.2
BuildRequires:    R-CRAN-broom >= 0.5.1
BuildRequires:    R-CRAN-purrr >= 0.3.4
BuildRequires:    R-CRAN-rlang >= 0.1.6
Requires:         R-stats >= 3.5.2
Requires:         R-CRAN-ggplot2 >= 2.2.1
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-tibble >= 1.4.2
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-semPlot >= 1.1
Requires:         R-CRAN-tidyr >= 0.8.0
Requires:         R-CRAN-dplyr >= 0.7.4
Requires:         R-CRAN-lavaan >= 0.6.2
Requires:         R-CRAN-broom >= 0.5.1
Requires:         R-CRAN-purrr >= 0.3.4
Requires:         R-CRAN-rlang >= 0.1.6

%description
Helper functions to implement univariate and bivariate latent change score
models in R using the 'lavaan' package. For details about Latent Change
Score Modeling (LCSM) see McArdle (2009)
<doi:10.1146/annurev.psych.60.110707.163612> and Grimm, An, McArdle,
Zonderman and Resnick (2012) <doi:10.1080/10705511.2012.659627>. The
package automatically generates 'lavaan' syntax for different model
specifications and varying timepoints. The 'lavaan' syntax generated by
this package can be returned and further specifications can be added
manually. Longitudinal plots as well as simplified path diagrams can be
created to visualise data and model specifications. Estimated model
parameters and fit statistics can be extracted as data frames. Data for
different univariate and bivariate LCSM can be simulated by specifying
estimates for model parameters to explore their effects. This package
combines the strengths of other R packages like 'lavaan', 'broom', and
'semPlot' by generating 'lavaan' syntax that helps these packages work
together.

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