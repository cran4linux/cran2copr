%global packname  binsreg
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          2%{?dist}
Summary:          Binscatter Estimation and Inference

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-sandwich 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-sandwich 

%description
Provides tools for statistical analysis using the binscatter methods
developed by Cattaneo, Crump, Farrell and Feng (2019a) <arXiv:1902.09608>
and Cattaneo, Crump, Farrell and Feng (2019b) <arXiv:1902.09615>.
Binscatter provides a flexible way of describing the mean relationship
between two variables based on partitioning/binning of the independent
variable of interest. binsreg() implements binscatter estimation and
robust (pointwise and uniform) inference of regression functions and
derivatives thereof, with particular focus on constructing binned scatter
plots. binsregtest() implements hypothesis testing procedures for
parametric functional forms of and nonparametric shape restrictions on the
regression function. binsregselect() implements data-driven procedures for
selecting the number of bins for binscatter estimation. All the commands
allow for covariate adjustment, smoothness restrictions and clustering.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
