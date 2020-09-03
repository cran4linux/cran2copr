%global packname  fbar
%global packver   0.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.0
Release:          1%{?dist}%{?buildtag}
Summary:          An Extensible Approach to Flux Balance Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-ROI 
BuildRequires:    R-CRAN-ROI.plugin.ecos 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-magrittr 
Requires:         R-Matrix 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-ROI 
Requires:         R-CRAN-ROI.plugin.ecos 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 

%description
A toolkit for Flux Balance Analysis and related metabolic modeling
techniques. Functions are provided for: parsing models in tabular format,
converting parsed metabolic models to input formats for common linear
programming solvers, and evaluating and applying gene-protein-reaction
mappings. In addition, there are wrappers to parse a model, select a
solver, find the metabolic fluxes, and return the results applied to the
original model. Compared to other packages in this field, this package
puts a much heavier focus on providing reusable components that can be
used in the design of new implementation of new techniques, in particular
those that involve large parameter sweeps. For a background on the theory,
see What is Flux Balance Analysis <doi:10.1038/nbt.1614>.

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
