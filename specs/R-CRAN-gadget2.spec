%global packname  gadget2
%global packver   2.3.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3.5
Release:          2%{?dist}%{?buildtag}
Summary:          Gadget is the Globally-Applicable Area Disaggregated GeneralEcosystem Toolbox

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core

%description
A statistical ecosystem modelling package, taking many features of the
ecosystem into account. Gadget works by running an internal model based on
many parameters, and then comparing the data from the output of this model
to real data to get a goodness-of-fit likelihood score. These parameters
can then be adjusted, and the model re-run, until an optimum is found,
which corresponds to the model with the lowest likelihood score. Gadget
allows the user to include a number of features into an ecosystem model:
One or more species, each of which may be split into multiple stocks;
multiple areas with migration between areas; predation between and within
species; maturation; reproduction and recruitment; multiple commercial and
survey fleets taking catches from the populations. For more details see
<https://hafro.github.io/gadget2>. This is the C++ Gadget2 runtime, making
it available for R.

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
