%global __brp_check_rpaths %{nil}
%global packname  esvis
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          3%{?dist}%{?buildtag}
Summary:          Visualization and Estimation of Effect Sizes

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildArch:        noarch
BuildRequires:    R-CRAN-tidyr >= 1.0.0
BuildRequires:    R-CRAN-sfsmisc 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-tidyr >= 1.0.0
Requires:         R-CRAN-sfsmisc 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-tibble 

%description
A variety of methods are provided to estimate and visualize distributional
differences in terms of effect sizes. Particular emphasis is upon
evaluating differences between two or more distributions across the entire
scale, rather than at a single point (e.g., differences in means). For
example, Probability-Probability (PP) plots display the difference between
two or more distributions, matched by their empirical CDFs (see Ho and
Reardon, 2012; <doi:10.3102/1076998611411918>), allowing for examinations
of where on the scale distributional differences are largest or smallest.
The area under the PP curve (AUC) is an effect-size metric, corresponding
to the probability that a randomly selected observation from the x-axis
distribution will have a higher value than a randomly selected observation
from the y-axis distribution. Binned effect size plots are also available,
in which the distributions are split into bins (set by the user) and
separate effect sizes (Cohen's d) are produced for each bin - again
providing a means to evaluate the consistency (or lack thereof) of the
difference between two or more distributions at different points on the
scale. Evaluation of empirical CDFs is also provided, with built-in
arguments for providing annotations to help evaluate distributional
differences at specific points (e.g., semi-transparent shading). All
function take a consistent argument structure. Calculation of specific
effect sizes is also possible. The following effect sizes are estimable:
(a) Cohen's d, (b) Hedges' g, (c) percentage above a cut, (d) transformed
(normalized) percentage above a cut, (e) area under the PP curve, and (f)
the V statistic (see Ho, 2009; <doi:10.3102/1076998609332755>), which
essentially transforms the area under the curve to standard deviation
units. By default, effect sizes are calculated for all possible pairwise
comparisons, but a reference group (distribution) can be specified.

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
%{rlibdir}/%{packname}
