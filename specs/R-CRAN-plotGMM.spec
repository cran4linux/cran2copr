%global __brp_check_rpaths %{nil}
%global packname  plotGMM
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Visualizing Gaussian Mixture Models

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
Requires:         R-methods 
Requires:         R-CRAN-wesanderson 
Requires:         R-CRAN-amerika 
Requires:         R-CRAN-ggplot2 

%description
The main function, plot_GMM, is used for plotting output from Gaussian
mixture models (GMMs), including both densities and overlaying mixture
weight component curves from the fit GMM. The package also include the
function, plot_cut_point, which plots the cutpoint (mu) from the GMM over
a histogram of the distribution with several color options. Finally, the
package includes the function, plot_mix_comps, which is used in the
plot_GMM function, and can be used to create a custom plot for overlaying
mixture component curves from GMMs. For the plot_mix_comps function, usage
most often will be specifying the "fun" argument within "stat_function" in
a ggplot2 object.

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
