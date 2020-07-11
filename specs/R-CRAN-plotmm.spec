%global packname  plotmm
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Tidy Tools for Visualizing Mixture Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-wesanderson 
BuildRequires:    R-CRAN-amerika 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-patchwork 
Requires:         R-methods 
Requires:         R-CRAN-wesanderson 
Requires:         R-CRAN-amerika 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-patchwork 

%description
The main function, plot_mm(), is used for plotting output from mixture
models, including both densities and overlaying mixture weight component
curves from the fit models. In line with the tidyverse, the package also
includes the plot_cut_point() function to visualize the cutpoint (mu) from
the model over a histogram of the data density with several color options.
Finally, the package includes the plot_mix_comps() helper function, which
is used for both added customization as well as in the plot_mm() function.
Supported model objects include: 'mixtools', 'EMCluster', and 'flexmix',
with more from each forthcoming. Supported mixture model specifications
include mixtures of univariate Gaussians, multivariate Gaussians, Gammas,
logistic regressions, linear regressions, and Poisson regressions.

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
