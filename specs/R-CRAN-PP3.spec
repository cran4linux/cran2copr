%global packname  PP3
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          2%{?dist}
Summary:          Three-Dimensional Exploratory Projection Pursuit

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildRequires:    R-stats 
Requires:         R-stats 

%description
Exploratory projection pursuit is a method to discovers structure in
multivariate data. At heart this package uses a projection index to
evaluate how interesting a specific three-dimensional projection of
multivariate data (with more than three dimensions) is. Typically, the
main structure finding algorithm starts at a random projection and then
iteratively changes the projection direction to move to a more interesting
one. In other words, the projection index is maximised over the projection
direction to find the most interesting projection. This maximum is,
though, a local maximum. So, this code has the ability to restart the
algorithm from many different starting positions automatically. Routines
exist to plot a density estimate of projection indices over the runs, this
enables the user to obtain an idea of the distribution of the projection
indices, and, hence, which ones might be interesting. Individual
projection solutions, including those identified as interesting, can be
extracted and plotted individually. The package can make use of the
mclapply() function to execute multiple runs in parallel to speed up index
discovery. Projection pursuit is similar to independent component
analysis. This package uses a projection index that maximises an entropy
measure to look for projections that exhibit non-normality, and operates
on sphered data. Hence, information from this package is different from
that obtained from principal components analysis, but the rationale behind
both methods is similar. Nason, G. P. (1995) <doi:10.2307/2986135>.

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
