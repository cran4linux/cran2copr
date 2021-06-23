%global __brp_check_rpaths %{nil}
%global debug_package %{nil}
%global packname  stratifyR
%global packver   1.0-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          3%{?dist}%{?buildtag}
Summary:          Optimal Stratification of Univariate Populations

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-fitdistrplus 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-zipfR 
BuildRequires:    R-CRAN-actuar 
BuildRequires:    R-CRAN-triangle 
BuildRequires:    R-CRAN-mc2d 
Requires:         R-CRAN-fitdistrplus 
Requires:         R-stats 
Requires:         R-CRAN-zipfR 
Requires:         R-CRAN-actuar 
Requires:         R-CRAN-triangle 
Requires:         R-CRAN-mc2d 

%description
This implements the stratification of univariate populations under
stratified sampling designs using the method of Khan et al. (2002)
<doi:10.1177/0008068320020518>, Khan et al. (2008)
(<http://www.statcan.gc.ca/pub/12-001-x/2008002/article/10761-eng.pdf>)
and Khan et al. (2015) <doi:10.1080/02664763.2015.1018674>. It determines
the Optimum Strata Boundaries (OSB) and Optimum Sample Sizes (OSS) for the
study variable, y, using the best-fit frequency distribution of a survey
variable (if data is available) or a hypothetical distribution (if data is
not available). The method formulates the problem of determining the OSB
as mathematical programming problem which is solved by using a dynamic
programming technique. If a dataset of the population is available to the
surveyor, the method estimates its best-fit distribution and determines
the OSB and OSS under Neyman allocation directly. When the dataset is not
available, stratification is made based on the assumption that the values
of the study variable, y, are available as hypothetical realizations of
proxy values of y from recent surveys. Thus, it requires certain
distributional assumptions about the study variable. At present, it
handles stratification for the populations where the study variable
follows a continuous distribution, namely, Pareto, Triangular,
Right-triangular, Weibull, Gamma, Exponential, Uniform, Normal, Log-normal
and Cauchy distributions.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
