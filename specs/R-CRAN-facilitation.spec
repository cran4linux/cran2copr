%global packname  facilitation
%global packver   0.5.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.2
Release:          3%{?dist}
Summary:          A C++ Framework for Plant-Plant Interaction IBMs

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.14
BuildRequires:    R-Matrix 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-animation 
Requires:         R-CRAN-Rcpp >= 0.12.14
Requires:         R-Matrix 
Requires:         R-grid 
Requires:         R-CRAN-animation 

%description
A tool for simulating a variety of spatial individual-based models of
plant-plant interactions. User-created models can include any number of
species, each of which can be structured in any number of life-stages,
where each life-stage has specific death, growth and reproduction rates,
as well as specific interaction radius, dispersal radius, and interaction
effects over each other species/life-stage. Life stages were modeled so as
to be a stochastic, individual-based version of differential Matrix
Population Models (Caswell 2001, ISBN:0-87893-096-5). Interactions can be
positive (facilitation) or negative (competition) and can affect death
rates, growth rates or reproduction rates. Interactions from multiple
numbers are additive, so as to best approximate classic population
dynamics models such as the logistic model and Lotka-Volterra model
(Britton 2004, ISBN:9781852335366). All models work in continuous time,
implemented as an optimized version of the Gillespie algorithm (Gillespie
1976 <doi:10.1016/0021-9991(76)90041-3>) for independent exponential
times, and continuous space.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
