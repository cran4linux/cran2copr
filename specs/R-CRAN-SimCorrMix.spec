%global packname  SimCorrMix
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          2%{?dist}%{?buildtag}
Summary:          Simulation of Correlated Data with Multiple Variable TypesIncluding Continuous and Count Mixture Distributions

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-SimMultiCorrData >= 0.2.1
BuildRequires:    R-CRAN-BB 
BuildRequires:    R-CRAN-nleqslv 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-VGAM 
BuildRequires:    R-CRAN-triangle 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grid 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-SimMultiCorrData >= 0.2.1
Requires:         R-CRAN-BB 
Requires:         R-CRAN-nleqslv 
Requires:         R-MASS 
Requires:         R-CRAN-mvtnorm 
Requires:         R-Matrix 
Requires:         R-CRAN-VGAM 
Requires:         R-CRAN-triangle 
Requires:         R-CRAN-ggplot2 
Requires:         R-grid 
Requires:         R-stats 
Requires:         R-utils 

%description
Generate continuous (normal, non-normal, or mixture distributions),
binary, ordinal, and count (regular or zero-inflated, Poisson or Negative
Binomial) variables with a specified correlation matrix, or one continuous
variable with a mixture distribution.  This package can be used to
simulate data sets that mimic real-world clinical or genetic data sets
(i.e., plasmodes, as in Vaughan et al., 2009
<DOI:10.1016/j.csda.2008.02.032>).  The methods extend those found in the
'SimMultiCorrData' R package.  Standard normal variables with an imposed
intermediate correlation matrix are transformed to generate the desired
distributions. Continuous variables are simulated using either Fleishman
(1978)'s third order <DOI:10.1007/BF02293811> or Headrick (2002)'s fifth
order <DOI:10.1016/S0167-9473(02)00072-5> polynomial transformation method
(the power method transformation, PMT).  Non-mixture distributions require
the user to specify mean, variance, skewness, standardized kurtosis, and
standardized fifth and sixth cumulants.  Mixture distributions require
these inputs for the component distributions plus the mixing
probabilities.  Simulation occurs at the component level for continuous
mixture distributions.  The target correlation matrix is specified in
terms of correlations with components of continuous mixture variables.
These components are transformed into the desired mixture variables using
random multinomial variables based on the mixing probabilities.  However,
the package provides functions to approximate expected correlations with
continuous mixture variables given target correlations with the
components. Binary and ordinal variables are simulated using a
modification of ordsample() in package 'GenOrd'. Count variables are
simulated using the inverse CDF method.  There are two simulation pathways
which calculate intermediate correlations involving count variables
differently. Correlation Method 1 adapts Yahav and Shmueli's 2012 method
<DOI:10.1002/asmb.901> and performs best with large count variable means
and positive correlations or small means and negative correlations.
Correlation Method 2 adapts Barbiero and Ferrari's 2015 modification of
the 'GenOrd' package <DOI:10.1002/asmb.2072> and performs best under the
opposite scenarios.  The optional error loop may be used to improve the
accuracy of the final correlation matrix.  The package also contains
functions to calculate the standardized cumulants of continuous mixture
distributions, check parameter inputs, calculate feasible correlation
boundaries, and summarize and plot simulated variables.

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
