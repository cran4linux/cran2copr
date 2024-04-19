%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ADLP
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Accident and Development Period Adjusted Linear Pools for Actuarial Stochastic Reserving

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-methods 
Requires:         R-methods 

%description
Loss reserving generally focuses on identifying a single model that can
generate superior predictive performance. However, different loss
reserving models specialise in capturing different aspects of loss data.
This is recognised in practice in the sense that results from different
models are often considered, and sometimes combined. For instance,
actuaries may take a weighted average of the prediction outcomes from
various loss reserving models, often based on subjective assessments. This
package allows for the use of a systematic framework to objectively
combine (i.e. ensemble) multiple stochastic loss reserving models such
that the strengths offered by different models can be utilised
effectively. Our framework is developed in Avanzi et al. (2023). Firstly,
our criteria model combination considers the full distributional
properties of the ensemble and not just the central estimate - which is of
particular importance in the reserving context. Secondly, our framework is
that it is tailored for the features inherent to reserving data. These
include, for instance, accident, development, calendar, and claim maturity
effects. Crucially, the relative importance and scarcity of data across
accident periods renders the problem distinct from the traditional
ensemble techniques in statistical learning. Our framework is illustrated
with a complex synthetic dataset. In the results, the optimised ensemble
outperforms both (i) traditional model selection strategies, and (ii) an
equally weighted ensemble. In particular, the improvement occurs not only
with central estimates but also relevant quantiles, such as the 75th
percentile of reserves (typically of interest to both insurers and
regulators). Reference: Avanzi B, Li Y, Wong B, Xian A (2023) "Ensemble
distributional forecasting for insurance loss reserving"
<doi:10.48550/arXiv.2206.08541>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
