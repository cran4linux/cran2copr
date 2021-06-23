%global __brp_check_rpaths %{nil}
%global packname  BeyondBenford
%global packver   1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Compare the Goodness of Fit of Benford's and Blondeau Da Silva'sDigit Distributions to a Given Dataset

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 2.1.0
Requires:         R-CRAN-ggplot2 >= 2.1.0

%description
Allows to compare the goodness of fit of Benford's and Blondeau Da Silva's
digit distributions in a dataset. It is used to check whether the data
distribution is consistent with theoretical distributions highlighted by
Blondeau Da Silva or not (through the dat.distr() function): this ideal
theoretical distribution must be at least approximately followed by the
data for the use of Blondeau Da Silva's model to be well-founded. It also
enables to plot histograms of digit distributions, both observed in the
dataset and given by the two theoretical approaches (with the digit.ditr()
function). Finally, it proposes to quantify the goodness of fit via
Pearson's chi-squared test (with the chi2() function).

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
