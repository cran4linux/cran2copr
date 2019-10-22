%global packname  SimRepeat
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Simulation of Correlated Systems of Equations with MultipleVariable Types

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-SimMultiCorrData >= 0.2.1
BuildRequires:    R-CRAN-SimCorrMix >= 0.1.0
BuildRequires:    R-CRAN-BB 
BuildRequires:    R-CRAN-nleqslv 
BuildRequires:    R-MASS 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-VGAM 
BuildRequires:    R-CRAN-triangle 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grid 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-SimMultiCorrData >= 0.2.1
Requires:         R-CRAN-SimCorrMix >= 0.1.0
Requires:         R-CRAN-BB 
Requires:         R-CRAN-nleqslv 
Requires:         R-MASS 
Requires:         R-Matrix 
Requires:         R-CRAN-VGAM 
Requires:         R-CRAN-triangle 
Requires:         R-CRAN-ggplot2 
Requires:         R-grid 
Requires:         R-stats 
Requires:         R-utils 

%description
Generate correlated systems of statistical equations which represent
repeated measurements or clustered data.  These systems contain either: a)
continuous normal, non-normal, and mixture variables based on the
techniques of Headrick and Beasley (2004) <DOI:10.1081/SAC-120028431> or
b) continuous (normal, non-normal and mixture), ordinal, and count
(regular or zero-inflated, Poisson and Negative Binomial) variables based
on the hierarchical linear models (HLM) approach.  Headrick and Beasley's
method for continuous variables calculates the beta (slope) coefficients
based on the target correlations between independent variables and between
outcomes and independent variables.  The package provides functions to
calculate the expected correlations between outcomes, between outcomes and
error terms, and between outcomes and independent variables, extending
Headrick and Beasley's equations to include mixture variables.  These
theoretical values can be compared to the simulated correlations.  The HLM
approach requires specification of the beta coefficients, but permits
group and subject-level independent variables, interactions among
independent variables, and fixed and random effects, providing more
flexibility in the system of equations.  Both methods permit simulation of
data sets that mimic real-world clinical or genetic data sets (i.e.
plasmodes, as in Vaughan et al., 2009, <10.1016/j.csda.2008.02.032>). The
techniques extend those found in the 'SimMultiCorrData' and 'SimCorrMix'
packages. Standard normal variables with an imposed intermediate
correlation matrix are transformed to generate the desired distributions.
Continuous variables are simulated using either Fleishman's third-order
(<DOI:10.1007/BF02293811>) or Headrick's fifth-order
(<DOI:10.1016/S0167-9473(02)00072-5>) power method transformation (PMT).
Simulation occurs at the component-level for continuous mixture
distributions.  These components are transformed into the desired mixture
variables using random multinomial variables based on the mixing
probabilities.  The target correlation matrices are specified in terms of
correlations with components of continuous mixture variables.  Binary and
ordinal variables are simulated by discretizing the normal variables at
quantiles defined by the marginal distributions.  Count variables are
simulated using the inverse CDF method.  There are two simulation pathways
for the multi-variable type systems which differ by intermediate
correlations involving count variables.  Correlation Method 1 adapts Yahav
and Shmueli's 2012 method <DOI:10.1002/asmb.901> and performs best with
large count variable means and positive correlations or small means and
negative correlations.  Correlation Method 2 adapts Barbiero and Ferrari's
2015 modification of the 'GenOrd' package <DOI:10.1002/asmb.2072> and
performs best under the opposite scenarios.  There are three methods
available for correcting non-positive definite correlation matrices.  The
optional error loop may be used to improve the accuracy of the final
correlation matrices. The package also provides function to check
parameter inputs and summarize the simulated systems of equations.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
